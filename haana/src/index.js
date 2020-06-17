import React from 'react';
import ReactDOM from 'react-dom';
import {
  BrowserRouter as Router,
  Route
} from "react-router-dom";

import './index.css';
import OneStore from './components/OneStore';
import Home from './components/Home'

const routing = (
  <Router>
    <div>
      <Route path="/" component={Home} />
      <Route path="/store" component={OneStore} />
    </div>   
  </Router> )
ReactDOM.render(routing, document.getElementById('root'))
