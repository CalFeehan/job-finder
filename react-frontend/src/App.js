
import { Route } from 'react-router-dom'
import Navbar from "./components/Navbar"
import Dashboard from "./views/Dashboard";
import Search from "./views/Search";
import Contact from "./views/Contact";
import Applications from "./views/Applications"
import Profile from "./views/Profile"
import './styles/app.scss'

function App() {

  return (
      <div className="screen" >
        <div className="nav">
          <Navbar />
        </div>
        <div className="component-container">
            <Route path="/profile" component={(props) => <Profile {...props} />} />
            <Route path="/contact" component={(props) => <Contact {...props} />} />
            <Route path="/search" component={(props) => <Search {...props} />} />
            <Route path="/applications" component={(props) => <Applications {...props} />} />
            <Route exact path="/dashboard" component={(props) => <Dashboard {...props} />} />
        </div>
      </div>
  );
}

export default App;
