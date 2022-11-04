import './navbar.css';
import PersonIcon from "@material-ui/icons/Person"
import MessageIcon from '@material-ui/icons/Message';
import  IconButton  from '@material-ui/core/IconButton';

function Navbar(){
    return (
        <div className='navbar'>
           
                <IconButton>
                    <PersonIcon className='person_icon' fontSize='large'/>
                </IconButton>
                
                <h1>ReferUp</h1>

                <IconButton>
                    <MessageIcon className='message_icon' fontSize='large'/>
                </IconButton>
                
            
           
        </div>
        
    );
}
export default Navbar