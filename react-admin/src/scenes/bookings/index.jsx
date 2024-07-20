import { useTheme, Button, Box, Typography, } from "@mui/material";
import { DataGrid, GridToolbar } from "@mui/x-data-grid";
import Header from "../../components/Header";
import { tokens } from "../../theme";
import { useEffect, useState } from "react";
import dataProvider from "../PrivateRoute/PrivateRoute";

const Bookings = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    const columns = [
        { field: "id", headerName: "ID", flex: 0.5 },
        {
            field: "task_location",
            headerName: "Task Location",
            flex: 1,
            editable: true,
        },
        {
            field: "street_name",
            headerName: "Street Name",
            flex: 1,
            editable: true,
        },
        {
            field: "task_size",
            headerName: "Task Size",
            flex: 1,
            editable: true,
        },
        {
            field: "task_detail",
            headerName: "Task Detail",
            flex: 2,
            editable: true,
        },
        {
            field: "full_name",
            headerName: "Full Name",
            flex: 1,
            editable: true,
            cellClassName: "name-column--cell",
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
            field: "service_name",
            headerName: "Service Name",
            flex: 1,
            editable: true,
        },
        {
            field: "date_created",
            headerName: "Date Created",
            flex: 1,
            editable: true,
            type: "dateTime",
        },
        {
            field: "status",
            headerName: "Status",
            flex: 1,
            editable: true,
        },
    ];

    const [data, setData] = useState([]);
    const [selectionModel, setSelectionModel] = useState([]);

    useEffect(() => {
        fetch('/api/v1/booking')
            .then(res => res.json())
            .then(data => {
                setData(data);
            })
            .catch(error => {
                console.error("Error fetching data:", error);
            });
    }, []);


    // HANDLE ROW EDIT
    const handleCellEditCommit = (params) => {
        const { id, field, value } = params;
        const updatedFields = { [field]: value };
        saveDataToDB(id, updatedFields);
    };

    // HANDLE STATUS CHANGE
    const handleStatusChange = async (newStatus) => {
        const updatedData = data.map((row) => {
            if (selectionModel.includes(row.id)) {
                return { ...row, status: newStatus };
            }
            return row;
        });

        setData(updatedData);

        // Save changes to the database
        for (const id of selectionModel) {
            const updatedFields = { status: newStatus };
            await saveDataToDB(id, updatedFields);
        }
    };

    const saveDataToDB = (id, updatedFields) => {
        fetch(`/api/v1/booking/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(updatedFields),
        })
            .then(response => response.json())
            .then(data => {
                console.log("Success:", data);
                setData((prevData) =>
                    prevData.map((row) => (row.id === id ? { ...row, ...updatedFields } : row))
                );
            })
            .catch(error => {
                console.error("Error:", error);
            });
    };


    // HANDLE DELETE
    const handleDelete = async () => {
        const confirmDelete = window.confirm("Are you sure you want to delete the selected records?");
        if (confirmDelete) {
            try {
                for (const id of selectionModel) {
                    await dataProvider.deleteBookingRecord(id);
                }
                setData((prevData) => prevData.filter((row) => !selectionModel.includes(row.id)));
                setSelectionModel([]); // Clear selection after deletion
            } catch (error) {
                console.error("Error deleting records:", error);
            }
        }
    };


    // SEND EMAIL TO USERS
    const sendEmail = async () => {
        const sender = "experthandyman@fastmail.com";
        const subject = 'Expert Handyman';
        const message = "Your booking status has been updated.";
        const recipients = data.filter((row) => selectionModel.includes(row.id)).map((row) => row.email);

        fetch('/api/v1/email', {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                subject: subject,
                message: message,
                sender: sender,
                recipients: recipients,
            })
        })
            .then(response => response.json())
            .then(data => {
                console.log("Email sent successfully:", data);
            })
            .catch(error => {
                console.error("Error sending email:", error);
            });
    };


    return (
        <Box m="20px">
            <Header title="BOOKINGS" subtitle="Managing all bookings" />
            <Box
                position="relative"
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

                {selectionModel.length > 0 && (<Box
                    position="absolute"
                    top="-3%"
                    right="0"
                    display="flex"
                    gap="10px"
                    zIndex="1"
                >
                    {/* DELETE BUTTON */}
                    <Button
                        onClick={handleDelete}
                        sx={{
                            padding: "7px auto",
                            width: "110px",
                            textAlign: "center",
                            borderRadius: "4px",
                            backgroundColor: "crimson",
                            color: "white",
                            fontWeight: "bold",
                            border: "none",
                            "&:hover": {
                                backgroundColor: "darkorange",
                            },
                        }}
                    >
                        <Typography variant="h6">
                            Delete
                        </Typography>
                    </Button>
                    {/* Progressing button */}
                    <Button
                        onClick={() => handleStatusChange('Progressing')}
                        sx={{
                            padding: "7px auto",
                            width: "110px",
                            textAlign: "center",
                            borderRadius: "4px",
                            backgroundColor: "orange",
                            color: "white",
                            fontWeight: "bold",
                            border: "none",
                            "&:hover": {
                                backgroundColor: "darkorange",
                            },
                        }}
                    >
                        <Typography variant="h6">
                            Progressing
                        </Typography>
                    </Button>
                    {/* Approved button */}
                    <Button
                        onClick={() => {
                            handleStatusChange('Approved');
                            sendEmail();
                        }}
                        sx={{
                            padding: "7px auto",
                            width: "110px",
                            textAlign: "center",
                            borderRadius: "4px",
                            backgroundColor: "green",
                            color: "white",
                            fontWeight: "bold",
                            border: "none",
                            "&:hover": {
                                backgroundColor: "darkgreen",
                            },
                        }}
                    >
                        <Typography variant="h6">
                            Approved
                        </Typography>
                    </Button>
                </Box>
                )}

                <DataGrid
                    checkboxSelection
                    rows={data}
                    columns={columns}
                    components={{ Toolbar: GridToolbar }}
                    onCellEditCommit={handleCellEditCommit}
                    onSelectionModelChange={(newSelection) => {
                        setSelectionModel(newSelection);
                    }}
                />
            </Box>
        </Box>
    );
};

export default Bookings;
