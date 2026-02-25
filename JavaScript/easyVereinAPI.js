/**
 * This file contains some ready to use functions to use the API in js
 * Just import this file and call the functions to be happy
*/

let response
const version = 'stable'
const domain = 'easyverein.com'

/**
 * Get the token of a user to "login" the user
 * @param {string} username - Only required on first call or forceReload == true. The username of the user to login (should look like this: org_max@mustermann.de)
 * @param {string} password - Only required on first call or forceReload == true. The password of the user to login
 * @param {string} twoFA - Only required on first call or forceReload == true and if the 2FA ist required for the user. The 2FA one time password
 * @param {boolean} forceReload - Optional, force to request the token again from the API instead of getting it from the "cache" (This may be needed when the password was changed)
 * @returns {object|any} - An object containing the complete response of the API or anything else if an error occured
 */
export async function getToken (username, password, twoFA = '', forceReload = false, onError = (res) => {}) {
    if (forceReload || response === undefined) {
        // The user is not allready loged in
        const content = {username: username, password: password, '2FA': twoFA}
        const newResponse = await post('get-token', content, onError)
        
        if (newResponse !== undefined && newResponse.hasOwnProperty('token')) {
            response = newResponse
        }
    }
    return response
}

/**
 * Post to an API endpoint using fetch
 * 
 * @param {string} endpoint - The endpoint to post to
 * @param {object} content - The content to post
 * @returns {object|any} - An object containing the complete response of the API or anything else if an error occured
 */
export async function post (endpoint, content, onError = (res) => {}) {
    const url = _buildURL(endpoint)
    const res = await fetch(`${url}`, {
        method: 'POST',
        headers: _headers(),
        body: JSON.stringify(content)
    })

    return await _handleResponse(res, onError)
}

/**
 * Get some entries of any endpoint
 * 
 * @param {string} endpoint - The endpoint to get
 * @param {number|string} id - Optional: The id of the entry to retrive
 * @param {string} query - Optional: The query to limit the fields that should be get
 * @param {number} limit - Optional: The limit of max etries shown in one page
 * @param {number} page - Optional: The page to get
 * @param {string} params - Optional: More params like seach can be filled here
 * @param {function} onError - Optional: An function that will be called if somthing went wrong 
 * @returns {object|any} - An object containing the complete response of the API or anything else if an error occured
 */
export async function get (endpoint, id = '', query = '{*}', limit = 20, page = 1, params = '', onError = (res) => {}) {
    const url = _buildURL(endpoint)
    const res = await fetch(`${url}/${id}?query=${query}&limit=${limit}&page=${page}&${params}`, {
        method: 'GET',
        headers: _headers()
    })

    return await _handleResponse(res, onError)
}

/**
 * Patch some changes to an entry
 * 
 * @param {string} endpoint - The endpoint to patch to
 * @param {number|string} id - The id of the entry to change
 * @param {object} content - The content to patch
 * @param {function} onError - Optional: An function that will be called if somthing went wrong
 * @returns {object|any} - An object containing the complete response of the API or anything else if an error occured
 */
export async function patch (endpoint, id, content, onError = (res) => {}) {
    const url = `${_buildURL(endpoint)}/${id}`
    const res = await fetch(url, {
        method: 'PATCH',
        headers: _headers(),
        body: JSON.stringify(content)
    })

    return await _handleResponse(res, onError)
}

/**
 * Uploading a file in JS
 * NOTE: To upload a file, the entry for which the file is intended must exist - POSTing a file is not possible
 *
 * @param {string} endpoint - The endpoint to patch to
 * @param {number|string} id - The id of the entry to change
 * @param {File} file - A file object for the file to upload
 * @param {string} fieldName - The name of the field to upload the file to
 * @param {Function} onError - Optional: An function that will be called if somthing went wrong
 * @returns {object|any} - Either the return of onError or the response json
 */
export async function uploadFile (endpoint, id, file, fieldName, onError = (res) => {}) {
    const url = `${_buildURL(endpoint)}/${id}`
    // The header must be modified to inform the API about the file to upload (name and type)
    const headers = _headers()
    delete headers['Content-Type']
    headers['Content-Disposition'] = `attachment; name="${file.name}"; filename="${file.name}"`
    // Using formdata to upload the file - this is the only way the API recognize the file inside the body
    const fileFormData = new FormData()
    fileFormData.append(fieldName, file)
    const res = await fetch(url, {
        method: 'PATCH',
        headers: headers,
        body: fileFormData
    })

    return await _handleResponse(res, onError)
}

function _buildURL (endpoint) {
    return `https://${domain}/api/${version}/${endpoint}`
}

function _headers () {
    let authorization = {}
    try {
        authorization = {Authorization: `Token ${response.token}`}
    } catch {}
    return {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        ...authorization
    }
}

/**
 * Handles the response of the API using the response codes
 *
 * @param {Response} res - A response object returned by the build in fetch function
 * @param {Function} onError - Optional: An function that will be called if somthing went wrong
 * @returns {object|any} - Either the return of onError or the response json
 */
async function _handleResponse (res, onError) {
    if (![200, 201].includes(res.status)) {
        return onError(res)
    } else {
        return await res.json()
    }
}
