import { CssBaseline, ThemeProvider } from "@mui/material";
import { useState } from "react";
import { Route, Routes } from "react-router-dom";
import Bookings from "./scenes/bookings";
import Dashboard from "./scenes/dashboard";
import SingUp from "./scenes/signUpForm";
import Login from "./scenes/loginForm"
import Sidebar from "./scenes/global/Sidebar";
import Topbar from "./scenes/global/Topbar";
import Services from "./scenes/services";
import Users from "./scenes/users";
import { ColorModeContext, useMode } from "./theme";
import Calendar from "./scenes/calendar/calendar";



function App() {
    const [theme, colorMode] = useMode();
    const [isSidebar, setIsSidebar] = useState(true);

    return (
        <ColorModeContext.Provider value={colorMode}>
            <ThemeProvider theme={theme}>
                <CssBaseline />
                <div className="app">
                    <Sidebar isSidebar={isSidebar} />
                    <main className="content">
                        <Topbar setIsSidebar={setIsSidebar} />
                        <Routes>
                            <Route path="/" element={<Dashboard />} />
                            <Route path="/dashboard" element={<Dashboard />} />
                            <Route path="/users" element={<Users />} />
                            <Route path="/bookings" element={<Bookings />} />
                            <Route path="/services" element={<Services />} />
                            <Route path="/form" element={<SingUp />} />
                            <Route path="/calendar" element={<Calendar />} />
                        </Routes>
                    </main>
                </div>
            </ThemeProvider>
        </ColorModeContext.Provider>
    );
}

export default App;
