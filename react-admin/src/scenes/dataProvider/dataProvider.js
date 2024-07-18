// dataProvider.js
const createDataProvider = () => {
    return {
        // async getRecords({ paginationModel: { start = 0, pageSize } }) {
        //     // Adjust the database query as needed
        //     return db.query(`SELECT * FROM users LIMIT ?, ?`, [start, pageSize]);
        // },


        // DELETE USERS
        async deleteRecord(id) {
            try {
                const response = await fetch(`http://localhost:5000/api/v1/users/${id}`, {
                    method: 'DELETE',
                });

                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                const data = await response.json();
                console.log("Success:", data);
            } catch (error) {
                console.error("Error:", error);
            }
        },

        // DELETE BOOKINGS
        async deleteBookingRecord(id) {
            try {
                const response = await fetch(`http://localhost:5000/api/v1/booking/${id}`, {
                    method: 'DELETE',
                });

                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                const data = await response.json();
                console.log("Success:", data);
            } catch (error) {
                console.error("Error:", error);
            }
        }
    };
};

export default createDataProvider();
