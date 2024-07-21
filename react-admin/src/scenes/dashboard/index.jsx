// import DownloadOutlinedIcon from "@mui/icons-material/DownloadOutlined";
import DoneAllOutlinedIcon from '@mui/icons-material/DoneAllOutlined';
import PendingOutlinedIcon from '@mui/icons-material/PendingOutlined';
import WorkOutlineOutlinedIcon from '@mui/icons-material/WorkOutlineOutlined';
import ApprovalOutlinedIcon from '@mui/icons-material/ApprovalOutlined';
import { Box, Typography, useTheme } from "@mui/material";
import Header from "../../components/Header";
// import ProgressCircle from "../../components/ProgressCircle";
import StatBox from "../../components/StatBox";
import { tokens } from "../../theme";
import { useState, useEffect } from "react";


const Dashboard = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);


    const [userData, setUserData] = useState([]);
    const [totalUsers, setTotalUsers] = useState(0);

    const [data, setData] = useState([]);
    const [taskCount, setTaskCount] = useState({ completed: 0, pending: 0, in_progress: 0 });
    const [totalBookings, setTotalBookings] = useState(0);

    useEffect(() => {
        updateAnalytics();
    }, []);
    
    // USER DATA
    useEffect(() => {
        fetch('/api/v1/users')
            .then(res => res.json())
            .then(data => {
                console.log(data);
                const lastFiveUsers = data.slice(-5);
                setUserData(lastFiveUsers);
                setTotalUsers(data.length);
            })
            .catch(error => {
                console.error("Error fetching data:", error);
            });
    }, []);

    // BOOKING DATA
    useEffect(() => {
        fetch('/api/v1/booking')
            .then(res => res.json())
            .then(data => {
                console.log(data);
                const lastFiveBooking = data.slice(-6);
                setData(lastFiveBooking);
                setTotalBookings(data.length);
            })
            .catch(error => {
                console.error("Error fetching data:", error);
            });
    }, []);


    // FUNCTION TO COUNT EACH TASK STATUS AND DISPLAY WITH ANIMATION
    const updateAnalytics = () => {
        fetch("/api/v1/booking/task_counts")
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.json();
            })
            .then((data) => {
                setTaskCount(data);
            })
            .catch((error) => {
                console.error("There was a problem with the fetch operation:", error);
                alert("Failed to fetch task counts. Please try again later.");
            });
    };


    return (
        <Box m="20px 20px 50px 20px">
            {/* HEADER */}
            <Box display="flex" justifyContent="space-between" alignItems="center">
                <Header title="DASHBOARD" subtitle="Welcome to Ex. Handyman Services's Dashboard" />
                {/* download btn not needed now */}
                {/* <Box>
                    <Button
                        sx={{
                            backgroundColor: colors.blueAccent[700],
                            color: colors.grey[100],
                            fontSize: "14px",
                            fontWeight: "bold",
                            padding: "10px 20px",
                        }}
                    >
                        <DownloadOutlinedIcon sx={{ mr: "10px" }} />
                        Download Reports
                    </Button>
                </Box> */}
            </Box>


            {/* GRID & TABLES */}
            <Box
                display="grid"
                gridTemplateColumns="repeat(12, 1fr)"
                gridAutoRows="140px"
                gap="20px"
            >
                {/* ROW 1 */}
                <Box
                    gridColumn="span 3"
                    backgroundColor={colors.primary[400]}
                    display="flex"
                    alignItems="center"
                    justifyContent="center"
                >
                    {/* completed */}
                    <StatBox
                        id="completedTasks"
                        title={taskCount.completed}
                        subtitle="Completed Tasks"
                        progress="1"
                        increase="+14%"
                        icon={
                            <DoneAllOutlinedIcon
                                sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
                            />
                        }
                    />
                </Box>

                {/* Pending */}
                <Box
                    gridColumn="span 3"
                    backgroundColor={colors.primary[400]}
                    display="flex"
                    alignItems="center"
                    justifyContent="center"
                >
                    <StatBox
                        id="pendingTasks"
                        title={taskCount.pending}
                        subtitle="Pending Tasks"
                        progress="0.50"
                        increase="+21%"
                        icon={
                            <PendingOutlinedIcon
                                sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
                            />
                        }
                    />
                </Box>

                {/* Progressing */}
                <Box
                    gridColumn="span 3"
                    backgroundColor={colors.primary[400]}
                    display="flex"
                    alignItems="center"
                    justifyContent="center"
                >
                    <StatBox
                        id="inProgressTasks"
                        title={taskCount.in_progress}
                        subtitle="Progressing Tasks"
                        progress="0.30"
                        increase="+5%"
                        icon={
                            <ApprovalOutlinedIcon
                                sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
                            />
                        }
                    />
                </Box>
                <Box
                    gridColumn="span 3"
                    backgroundColor={colors.primary[400]}
                    display="flex"
                    alignItems="center"
                    justifyContent="center"
                >
                    {/* Total Bookings */}
                    <StatBox
                        title={totalBookings}
                        subtitle="Total Bookings"
                        progress="0.80"
                        increase="+43%"
                        icon={
                            <WorkOutlineOutlinedIcon
                                sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
                            />
                        }
                    />
                </Box>

                {/* ROW 2 */}
                {/* Recent Booking Table */}
                <Box
                    gridColumn="span 8"
                    gridRow="span 3"
                    backgroundColor={colors.primary[400]}
                    overflow="auto"
                    position="relative"
                    borderRadius={1}
                >
                    <Box
                        display="flex"
                        justifyContent="space-between"
                        alignItems="center"
                        borderBottom={`4px solid ${colors.primary[500]}`}
                        colors={colors.grey[100]}
                        p="15px"
                        position="sticky"
                        top="0"
                        backgroundColor={colors.primary[400]}
                    >
                        <Typography color={colors.grey[100]} variant="h5" fontWeight="600">
                            Recent Bookings
                        </Typography>
                    </Box>
                    {data.map((row, i) => (
                        <Box
                            key={`${row.id}-${i}`}
                            display="flex"
                            justifyContent="space-between"
                            alignItems="center"
                            borderBottom={`4px solid ${colors.primary[500]}`}
                            p="15px"
                        >
                            <Box>
                                <Typography
                                    color={colors.greenAccent[500]}
                                    variant="h5"
                                    fontWeight="600"
                                >
                                    {row.id}
                                </Typography>
                                <Typography color={colors.grey[100]}>
                                    {row.service_name}
                                </Typography>
                            </Box>
                            <Box display='flex' alignItems='left' justifyContent="left" color={colors.grey[100]}>{row.street_name}</Box>
                            <Box display='flex' alignItems='left' justifyContent="left" color={colors.grey[100]}>{row.email}</Box>
                            <Box display='flex' alignItems='left' justifyContent="left" color={colors.grey[100]}>
                            <Typography
                                    color={colors.greenAccent[600]}
                                    variant="h5"
                                    fontWeight="600"
                                >
                                    {row.phone}
                                </Typography>
                            </Box>
                        </Box>
                    ))}
                </Box>

                {/* Recent Users Table */}
                <Box
                    gridColumn="span 4"
                    gridRow="span 2"
                    backgroundColor={colors.primary[400]}
                    overflow="auto"
                    position="relative"
                    borderRadius={3}
                >
                    <Box
                        display="flex"
                        justifyContent="space-between"
                        alignItems="center"
                        borderBottom={`4px solid ${colors.primary[500]}`}
                        colors={colors.grey[100]}
                        p="15px"
                        position="sticky"
                        top="0"
                        backgroundColor={colors.primary[400]}
                    >
                        <Typography color={colors.grey[100]} variant="h5" fontWeight="600">
                            Recent Users
                        </Typography>
                    </Box>
                    {userData.map((row, i) => (
                        <Box
                            key={`${row.id}-${i}`}
                            display="flex"
                            justifyContent="space-between"
                            alignItems="center"
                            borderBottom={`4px solid ${colors.primary[500]}`}
                            p="15px"
                        >
                            <Box>
                                <Typography
                                    color={colors.greenAccent[500]}
                                    variant="h5"
                                    fontWeight="600"
                                >
                                    {row.id}
                                </Typography>
                            </Box>
                            <Box>
                                <Typography color={colors.grey[100]}>
                                    {row.first_name}
                                </Typography>
                            </Box>
                            <Box
                                backgroundColor={colors.greenAccent[600]}
                                p="5px 10px"
                                borderRadius="4px"
                            >
                                {row.phone}
                            </Box>
                        </Box>
                    ))}
                </Box>

                {/* ROW 3 */}
                <Box
                    gridColumn="span 4"
                    gridRow="span 1"
                    backgroundColor={colors.primary[400]}
                    p="30px"

                >
                    <Typography fontSize=".9rem" borderRadius="5px" padding="6px" variant="h6" fontWeight="600" backgroundColor={colors.greenAccent[500]} textAlign="center">
                        Total Number Of Users
                    </Typography>
                    <Box
                        display="flex"
                        flexDirection="column"
                        alignItems="center"
                        mt="25px"
                    >
                        <Typography
                            variant="h1"
                            color={colors.greenAccent[500]}
                            sx={{ mt: "-5px", mb:"10px", fontWeight: "700" }}
                        >
                            {totalUsers}
                        </Typography>
                        {/* <Typography sx={{ mt:"-8px" }}>All user who can see their profiles</Typography> */}
                    </Box>
                </Box>
            </Box>
        </Box>
    );
};

export default Dashboard;
