import {Grid} from "@material-ui/core"
import Navbar from "./components/Navbar"
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import Dashboard from "./views/Dashboard";
import './styles/app.scss'

function App() {

  return (
    <BrowserRouter >
      <Grid container style={{height: "100%"}}>
        <Grid item component={Navbar}/>
        <Grid item  style={{flexGrow: 1, background: "#EAEAEA"}}>
          <Switch>
            <Route path="/" component={(props) => <Dashboard {...props} />} />
          </Switch>
        </Grid>
      </Grid>
    </BrowserRouter>
  );
}

export default App;
