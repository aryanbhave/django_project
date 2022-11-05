import React from 'react';
import "./App.css"



function SimpleTable(props) {

    
    
    return (
        <div>
                <table class="table" id="tablestyle">
                    <thead>
                        <tr>
                        <th scope="col">#</th>
                        <th scope="col">Company</th>
                        <th scope="col">Contact</th>
                        <th scope="col">Country</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                        <th scope="row">1</th>
                        <td>Google</td>
                        <td>Juan</td>
                        <td>USA</td>
                        </tr>
                        <tr>
                        <th scope="row">2</th>
                        <td>Meta</td>
                        <td>Shaunak</td>
                        <td>USA</td>
                        </tr>
                        <tr>
                        <th scope="row">3</th>
                        <td>Amazon</td>
                        <td>Shaitra</td>
                        <td>USA</td>
                        </tr>

                        <tr>
                        <th scope="row">4</th>
                        <td><input class="form-control" type="text" placeholder="Company" readonly/></td>
                        <td><input class="form-control" type="text" placeholder="Contact" readonly/></td>
                        
                        <td><input class="form-control" type="text" placeholder="Country" readonly/></td>
    
                        </tr>

                        
                    
                    
                    
                    </tbody>
                </table>
                <div id="buttonTable" > 
                <button type="button" class="btn btn-outline-primary">Submit</button>
                </div>
              
   
            
        </div>
    );
}

export default SimpleTable;