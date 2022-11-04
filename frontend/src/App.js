import React from "react";
import Navbar from "./Navbar";
import './navbar.css';
import CardComponent from "./CardComponent";
import SimpleTable from "./SimpleTable"

import { BrowserRouter as Router,Routes,Route,Link} from "react-router-dom";
import { Table } from "@mui/material";

function App() {
  return (
         
      <SimpleTable/>     
      
  );
}

export default App;
