import {Grid} from "@material-ui/core"

function App() {

  return (
    <>
      <Grid container style={{height: "100%"}}>
        <Grid item style={{width: "3.5rem", background: "red"}}>

        </Grid>
        <Grid item style={{flexGrow: 1, background: "blue"}}>
          
        </Grid>
      </Grid>
    </>
  );
}

export default App;
