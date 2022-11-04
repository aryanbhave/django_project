import React from 'react';
import { DataGrid } from '@mui/x-data-grid';
import ReactTable from "react-table";  



function SimpleTable(props) {
    const data = [{  
        name: 'Ayaan',  
        age: 26  
        },{  
        name: 'Ahana',  
        age: 22  
        },{  
        name: 'Peter',  
        age: 40   
        },{  
        name: 'Virat',  
        age: 30  
        },{  
        name: 'Rohit',  
        age: 32  
        },{  
        name: 'Dhoni',  
        age: 37  
        }]  

        const columns = [{  
            Header: 'Name',  
            accessor: 'name'  
           },{  
           Header: 'Age',  
           accessor: 'age'  
           }]  
    
    
    return (
        <div>
            <ReactTable  
            data={data}  
            columns={columns}  
            defaultPageSize = {2}  
            pageSizeOptions = {[2,4, 6]}  
           />  
            
        </div>
    );
}

export default SimpleTable;