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
import axios from 'axios';


const Dashboard = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    const [userData, setUserData] = useState([]);
    const [totalUsers, setTotalUsers] = useState(0);

    const [data, setData] = useState([]);
    const [taskCount, setTaskCount] = useState({ Approved: 0, Pending: 0, Progressing: 0 });
    const [totalBookings, setTotalBookings] = useState(0);

    const apiUrl = process.env.REACT_APP_API_BASE_URL;

    useEffect(() => {
        updateAnalytics();
    }, []);

    // USER DATA
    useEffect(() => {
        axios.get(`${apiUrl}/api/v1/users`)
            .then(res => {
                console.log(res.data);
                const lastFiveUsers = res.data.slice(-5);
                setUserData(lastFiveUsers);
                setTotalUsers(res.data.length);
            })
            .catch(error => {
                console.error("Error fetching data:", error);
            });
    }, [apiUrl]);

    // BOOKING DATA
    useEffect(() => {
        axios.get(`${apiUrl}/api/v1/bookings`)
            .then(res => {
                console.log(res.data);
                setTotalBookings(res.data.length);
                const lastFiveBooking = res.data.slice(-10);
                setData(lastFiveBooking);
            })
            .catch(error => {
                console.error("Error fetching data:", error);
            });
    }, [apiUrl]);

    // FUNCTION TO COUNT EACH TASK STATUS AND DISPLAY WITH ANIMATION
    const updateAnalytics = () => {
        axios.get(`${apiUrl}/api/v1/bookings/task_counts`)
            .then(res => {
                setTaskCount(res.data);
            })
            .catch(error => {
                console.error("There was a problem with the fetch operation:", error);
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
                        title={taskCount.Approved}
                        subtitle="Completed Tasks"
                        progress={`${taskCount.Approved / totalBookings}`}
                        const increase = {`${((taskCount.Approved / totalBookings) * 100).toFixed(1)}%`}
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
                        title={taskCount.Pending}
                        subtitle="Pending Tasks"
                        progress={`${taskCount.Pending / totalBookings}`}
                        const increase = {`${((taskCount.Pending / totalBookings) * 100).toFixed(1)}%`}
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
                        title={taskCount.Progressing}
                        subtitle="Progressing Tasks"
                        progress={`${taskCount.Progressing / totalBookings}`}
                        const increase = {`${((taskCount.Progressing / totalBookings) * 100).toFixed(1)}%`}
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
                        progress={`${totalBookings / totalBookings}`}
                        increase={`${((totalBookings / totalBookings) * 100).toFixed(1)}%`}
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
