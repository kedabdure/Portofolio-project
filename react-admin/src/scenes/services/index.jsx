import { Box, Typography, useTheme } from "@mui/material";
import { DataGrid, GridToolbar } from "@mui/x-data-grid";
import Header from "../../components/Header";
import { tokens } from "../../theme";
import { useState, useEffect } from "react";


const Services = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    const columns = [
        { field: "id", headerName: "ID" },
        {
            field: "first_name",
            headerName: "First Name",
            flex: 1,
            cellClassName: "name-column--cell",
        },
        {
            field: "last_name",
            headerName: "Last Name",
            flex: 1,
            editable: true,
        },
        {
            field: "email",
            headerNaServicesme: "Email",
            flex: 1,
            editable: true,
        },
        {
            field: "phone",
            headerName: "Phone Number",
            flex: 1,
            renderCell: (params) => (
                <Typography color={colors.greenAccent[500]}>
                    📱{params.row.phone}
                </Typography>
            ),
        },
    ];

    const [adminsData, setAdminsData] = useState([]);

    useEffect(() => {
        fetch('http://localhost:5000/api/v1/admins')
            .then(res => res.json())
            .then(data => {
                setAdminsData(data);
            })
            .catch(error => {
                console.error("Error fetching data:", error);
            });
    }, []);


    return (
        <Box m="20px">
            <Header title="SERVICES" subtitle="List of services we offer" />
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
                    checkboxSelection
                    rows={adminsData}
                    columns={columns}
                    components={{ Toolbar: GridToolbar }} />
            </Box>
        </Box>
    );
};

export default Services;
