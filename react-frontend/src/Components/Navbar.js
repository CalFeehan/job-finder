import { Button, Grid } from "@material-ui/core"
import { useState } from 'react'

export default function Navbar(props) {
    const [isDashboardHover, setDashboardHover] = useState(false);
    const [isProfileHover, setProfileHover] = useState(false);
    const [isContactHover, setContactHover] = useState(false);
    const [isLogoutHover, setLogoutHover] = useState(false);

    return (
            <Grid container direction="column" style={{width: "3.5rem", background: "#2F4067"}} {...props}>
                <Grid style={{width: "3.5rem", height: "3.5rem", minWidth: "unset", background: "url('/assets/Logo.png')", backgroundRepeat: "no-repeat", backgroundSize: "50%", backgroundPosition: "center", margin: "1rem 0rem 1rem 0rem"}}/>
                <Grid item container justifyContent= "center" direction="column" style={{flexGrow: 1}}>
                    <Button
                    onMouseEnter={() => setDashboardHover(true)}
                    onMouseLeave={() => setDashboardHover(false)}
                    style={{width: "3.5rem", height: "3.5rem", minWidth: "unset", background: "url('/assets/Icon-dashboard.png')", backgroundRepeat: "no-repeat", backgroundSize: "50%", backgroundPosition: "center", margin: "1rem 0rem 1rem 0rem"}}/>
                    {isDashboardHover && (
                        <div style={{position: "absolute", color: "#2F4067", margin: "0rem 0rem 10.5rem 4rem", fontWeight: "bold"}}>
                            Dashboard
                        </div> )}
                    <Button 
                    onMouseEnter={() => setProfileHover(true)}
                    onMouseLeave={() => setProfileHover(false)}
                    style={{width: "3.5rem", height: "3.5rem", minWidth: "unset", background: "url('/assets/Icon-profile.png')", backgroundRepeat: "no-repeat", backgroundSize: "50%", backgroundPosition: "center", margin: "1rem 0rem 1rem 0rem"}}/>
                    {isProfileHover && (
                        <div style={{position: "absolute", color: "#2F4067", margin: "0rem 0rem 0rem 4rem", fontWeight: "bold"}}>
                            Profile
                        </div> )}
                    <Button
                    onMouseEnter={() => setContactHover(true)}
                    onMouseLeave={() => setContactHover(false)}
                    style={{width: "3.5rem", height: "3.5rem", minWidth: "unset", background: "url('/assets/Icon-contact.png')", backgroundRepeat: "no-repeat", backgroundSize: "50%", backgroundPosition: "center", margin: "1rem 0rem 1rem 0rem"}}/>
                    {isContactHover && (
                        <div style={{position: "absolute", color: "#2F4067", margin: "10.5rem 0rem 0rem 4rem", fontWeight: "bold"}}>
                            Contact
                        </div> )}
                </Grid>
                <Button 
                onMouseEnter={() => setLogoutHover(true)}
                onMouseLeave={() => setLogoutHover(false)}
                style={{width: "3.5rem", height: "3.5rem", minWidth: "unset", background: "url('/assets/Icon-logout.png')", backgroundRepeat: "no-repeat", backgroundSize: "50%", backgroundPosition: "center", margin: "1rem 0rem 1rem 0rem"}}/>
                {isLogoutHover && (
                        <div style={{position: "absolute", color: "#2F4067", bottom: "0px", margin: "0rem 0rem 2rem 4rem", fontWeight: "bold"}}>
                            Logout
                        </div> )}
            </Grid>
    );
}
