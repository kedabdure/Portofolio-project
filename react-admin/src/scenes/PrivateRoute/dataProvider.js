import axios from 'axios';

const API_URL = process.env.REACT_APP_API_BASE_URL;
console.log(API_URL);

const dataProvider = {
    // Booking Records
    createBookingRecord: async (data) => {
        try {
            const response = await axios.post(`${API_URL}/api/v1/bookings`, data);
            return response.data;
        } catch (error) {
            console.error("Error creating booking record:", error);
            throw error;
        }
    },
    getBookingRecords: async () => {
        try {
            const response = await axios.get(`${API_URL}/api/v1/bookings`);
            return response.data;
        } catch (error) {
            console.error("Error fetching booking records:", error);
            throw error;
        }
    },
    updateBookingRecord: async (id, data) => {
        try {
            const response = await axios.put(`${API_URL}/api/v1/bookings/${id}`, data);
            console.log("Update Response:", response.data);
            return response.data;
        } catch (error) {
            console.error("Error updating booking record:", error.response ? error.response.data : error.message);
            throw error;
        }
    },
    deleteBookingRecord: async (id) => {
        try {
            const response = await axios.delete(`${API_URL}/api/v1/bookings/${id}`);
            return response.data;
        } catch (error) {
            console.error("Error deleting booking record:", error);
            throw error;
        }
    },
    // User Records
    createUserRecord: async (data) => {
        try {
            const response = await axios.post(`${API_URL}/api/v1/users`, data);
            return response.data;
        } catch (error) {
            console.error("Error creating user record:", error);
            throw error;
        }
    },
    getUserRecords: async () => {
        try {
            const response = await axios.get(`${API_URL}/api/v1/users`);
            return response.data;
        } catch (error) {
            console.error("Error fetching user records:", error);
            throw error;
        }
    },
    updateUserRecord: async (id, data) => {
        try {
            const response = await axios.put(`${API_URL}/api/v1/users/${id}`, data);
            console.log("Update Response:", response.data);
            return response.data;
        } catch (error) {
            console.error("Error updating user record:", error.response ? error.response.data : error.message);
            throw error;
        }
    },
    deleteUserRecord: async (id) => {
        try {
            const response = await axios.delete(`${API_URL}/api/v1/users/${id}`);
            return response.data;
        } catch (error) {
            console.error("Error deleting user record:", error);
            throw error;
        }
    }
};

export default dataProvider;
