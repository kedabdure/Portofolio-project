import { Box, useTheme } from "@mui/material";
import { GridToolbar } from '@mui/x-data-grid/components';
import { DataGrid } from "@mui/x-data-grid";
import Header from "../../components/Header";
import { tokens } from "../../theme";
import { useEffect, useState } from "react";
import dataProvider from '../PrivateRoute/dataProvider';
import DeleteOutlinedIcon from '@mui/icons-material/DeleteOutlined';
import axios from "axios";

const Users = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    const columns = [
        { field: "id", headerName: "ID" },
        {
            field: "first_name",
            headerName: "First name",
            flex: 1,
            cellClassName: "name-column--cell",
            editable: true,
        },
        {
            field: "last_name",
            headerName: "Last name",
            flex: 1,
            cellClassName: "name-column--cell",
            editable: true,
        },
        {
            field: "email",
            headerName: "Email",
            flex: 1,
            editable: true,
        },
        {
            field: "phone",
            headerName: "Phone Number",
            flex: 1,
            editable: true,
        },
        {
            field: "date_created",
            headerName: "Date",
            flex: 1,
        },
        {
            field: "is_admin",
            headerName: "Is User",
            flex: 1,
            editable: true,
        },
        {
            // field: "actions",
            headerName: "Action",
            renderCell: (params) => (
                <button
                    style={{ backgroundColor: "transparent", border: "none", m: "0 auto", padding: "0 auto" }} >
                    <DeleteOutlinedIcon
                        sx={{ color: "crimson", fontSize: "26px", cursor: "pointer" }}
                        onClick={() => handleDelete(params.id)}
                    />
                </button>
            ),
        },
    ];

    const [data, setData] = useState([]);
    const apiUrl = process.env.REACT_APP_API_BASE_URL;


    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get(`${apiUrl}/api/v1/users`);
                // console.log(response)
                setData(response.data)
            } catch (error) {
                console.error("Error fetching user records:", error);
                throw error;
            }
        };
        fetchData();
    }, [apiUrl]);


    // HANDLE ROW EDIT
    const processRowUpdate = async (newRow, oldRow) => {
        const { id, ...updatedFields } = newRow;

        try {
            await dataProvider.updateUserRecord(id, updatedFields);
            return newRow;
        } catch (error) {
            console.error("Error updating record:", error);
            return oldRow;
        }
    };


    // HANDLE DELETE
    const handleDelete = async (id) => {
        const confirmDelete = window.confirm("Are you sure you want to delete this record?");
        if (confirmDelete) {
            try {
                console.log(`Deleting record with ID: ${id}`);
                const response = await dataProvider.deleteUserRecord(id);
                console.log(`API response for ID ${id}:`, response);
    
                setData((prevData) => prevData.filter((row) => row.id !== id));
            } catch (error) {
                console.error("Error deleting record:", error);
            }
        }
    };
    

    return (
        <Box m="20px">
            <Header title="USERS" subtitle="Managing all users" />
            <Box
                m="40px 0 0 0"
                height="75vh"
                sx={{
                    "& .MuiDataGrid-root": {
                        border: "none",
                    },
                    "& .MuiDataGrid-cell": {
                        borderBottom: "none",
                    },
                    "& .name-column--cell": {
                        color: colors.greenAccent[300],
                    },
                    "& .MuiDataGrid-columnHeaders": {
                        backgroundColor: colors.blueAccent[700],
                        borderBottom: "none",
                    },
                    "& .MuiDataGrid-virtualScroller": {
                        backgroundColor: colors.primary[400],
                    },
                    "& .MuiDataGrid-footerContainer": {
                        borderTop: "none",
                        backgroundColor: colors.blueAccent[700],
                    },
                    "& .MuiCheckbox-root": {
                        color: `${colors.greenAccent[200]} !important`,
                    },
                    "& .MuiDataGrid-toolbarContainer .MuiButton-text": {
                        color: `${colors.grey[100]} !important`,
                    },
                }}
            >
                <DataGrid
                    // checkboxSelection
                    rows={data}
                    columns={columns}
                    components={{ Toolbar: GridToolbar }}
                    processRowUpdate={processRowUpdate}
                />
            </Box>
        </Box>
    );
};

export default Users;
