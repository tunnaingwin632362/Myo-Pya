import axios from 'axios'

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL
})

// Attach token to every request
api.interceptors.request.use(config => {
    const token = localStorage.getItem('token')
    if (token) config.headers.Authorization = `Bearer ${token}`
    return config
})

export const listingsApi = {
    getAll: (params) => api.get('/api/listings', { params }),
    getOne: (id) => api.get(`/api/listings/${id}`),
    create: (data) => api.post('/api/listings', data),
    update: (id, data) => api.put(`/api/listings/${id}`, data),
    delete: (id) => api.delete(`/api/listings/${id}`)
}

export const agentsApi = {
    getAll: () => api.get('/api/agents'),
    create: (data) => api.post('/api/agents', data),
    update: (id, data) => api.put(`/api/agents/${id}`, data),
    delete: (id) => api.delete(`/api/agents/${id}`)
}

export const authApi = {
    login: (data) => api.post('/api/auth/login', data),
    register: (data) => api.post('/api/auth/register', data)
}

export const inquiriesApi = {
    create: (data) => api.post('/api/inquiries', data),
    getAll: () => api.get('/api/inquiries'),
    markRead: (id) => api.put(`/api/inquiries/${id}/read`)
}

export const uploadApi = {
    uploadImage: (file) => {
    const form = new FormData()
    form.append('file', file)
    return api.post('/api/upload/image', form)
    }
}

export default api