import './navbar.css';

function Navbar(){
    return (
        <div className='navbar'>
            <div className='branding'>
                <h1>Referrals App</h1>
            </div>
            <div className='loginButton'>
                <button class='btn btn-primary' className='loginButton button4'>
                    Login
                </button>
            </div>
        </div>
        
    );
}
export default Navbar