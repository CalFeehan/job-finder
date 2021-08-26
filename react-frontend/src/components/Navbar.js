import { Button, Grid } from "@material-ui/core"
import "../styles/app.scss"


export default function Navbar(props) {

    const buttonStyle = {width: "3.5rem", height: "3.5rem", minWidth: "unset", backgroundRepeat: "no-repeat", backgroundSize: "40%", backgroundPosition: "center", margin: "1rem 0rem 1rem 0rem"};
    const hoverStyle = {position: "fixed", color: "#2F4067", fontWeight: "bold"};

    return (
            <Grid container direction="column" style={{width: "3.5rem", background: "#2F4067"}} {...props}>

                <Grid style={Object.assign({background: "url('/assets/Logo.png')"}, buttonStyle)}/>

                <Grid item container justifyContent= "center" direction="column" style={{flexGrow: 1}}>

                    <Button className="dashboard-button" 
                    style={Object.assign({background: "url('/assets/Icon-dashboard.png')"}, buttonStyle)} />
                    <div className="dashboard-hover" style={Object.assign({margin: "-5.25rem 0rem 0rem 4rem"}, hoverStyle)}> Dashboard </div>

                    <Button className="profile-button" 
                    style={Object.assign({background: "url('/assets/Icon-profile.png')"}, buttonStyle)} />
                    <div className="profile-hover" style={Object.assign({margin: "0rem 0rem 0rem 4rem"}, hoverStyle)}> Profile </div>

                    <Button className="contact-button" 
                    style={Object.assign({background: "url('/assets/Icon-contact.png')"}, buttonStyle)} />
                    <div className="contact-hover" style={Object.assign({margin: "5.25rem 0rem 0rem 4rem"}, hoverStyle)}> Contact </div>

                </Grid>

                <Button className="logout-button" 
                style={Object.assign({background: "url('/assets/Icon-logout.png')"}, buttonStyle)} />
                <div className="logout-hover" style={Object.assign({bottom: "0px", margin: "0rem 0rem 2rem 4rem"}, hoverStyle)}> Logout </div>

            </Grid>
    );
}
