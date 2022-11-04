import React,{useState} from 'react';
import TinderCard from "react-tinder-card";
import { DataGrid } from '@mui/x-data-grid';




function  CardComponent(){
    const {companies,setCompanies} = useState([
        {
            name:'Google',
            url:''
        },
        {
            name:'Facebook',
            url:'./images/facebook.jpg'
    
        }
        
    
    ]);
    return (
        
        <div>
             


      
           

  
            
        </div>
        
    );
    
};

export default CardComponent;