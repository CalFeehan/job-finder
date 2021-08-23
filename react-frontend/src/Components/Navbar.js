import { Button, Grid } from "@material-ui/core"

export default function Navbar(props) {


    return (
        <Grid container direction="column" style={{width: "3.5rem", background: "#2F4067"}} {...props}>
            <Grid style={{width: "3.5rem", height: "3.5rem", minWidth: "unset", background: "url('/assets/Logo.png')", backgroundRepeat: "no-repeat", backgroundSize: "50%", backgroundPosition: "center", margin: "1rem 0rem 1rem 0rem"}}/>
            <Grid item container justifyContent= "center" direction="column" style={{flexGrow: 1}}>
                <Button style={{width: "3.5rem", height: "3.5rem", minWidth: "unset", background: "url('/assets/Icon-dashboard.png')", backgroundRepeat: "no-repeat", backgroundSize: "50%", backgroundPosition: "center", margin: "1rem 0rem 1rem 0rem"}}/>
                <Button style={{width: "3.5rem", height: "3.5rem", minWidth: "unset", background: "url('/assets/Icon-profile.png')", backgroundRepeat: "no-repeat", backgroundSize: "50%", backgroundPosition: "center", margin: "1rem 0rem 1rem 0rem"}}/>
                <Button style={{width: "3.5rem", height: "3.5rem", minWidth: "unset", background: "url('/assets/Icon-contact.png')", backgroundRepeat: "no-repeat", backgroundSize: "50%", backgroundPosition: "center", margin: "1rem 0rem 1rem 0rem"}}/>
            </Grid>
            <Button style={{width: "3.5rem", height: "3.5rem", minWidth: "unset", background: "url('/assets/Icon-logout.png')", backgroundRepeat: "no-repeat", backgroundSize: "50%", backgroundPosition: "center", margin: "1rem 0rem 1rem 0rem"}}/>

        </Grid>
    )
}
