import "../styles/app.scss"
import {useHistory} from 'react-router-dom';

export default function Navbar(props) {

    const history = useHistory();
    
    return (

            <div className="navbar">
                <div className="logo"></div>

                <div className="nav-buttons"> 

                    <button className="dashboard-button" 
                    onClick={()=>history.push("/dashboard")}/>

                    <button className="profile-button" 
                    onClick={()=>history.push("/profile")}/>

                    <button className="contact-button" 
                    onClick={()=>history.push("/contact")}/>

                </div>

                <button className="logout-button" />

            </div>
            
    );
}
