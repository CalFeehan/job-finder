import {Grid} from "@material-ui/core"
import Navbar from "./components/Navbar"

function App() {

  return (
    <>
      <Grid container style={{height: "100%"}}>
        <Grid item component={Navbar}/>
        <Grid item style={{flexGrow: 1, background: "#EAEAEA"}}>
          
        </Grid>
      </Grid>
    </>
  );
}

export default App;
