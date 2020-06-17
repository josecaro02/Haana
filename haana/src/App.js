import React, { Component } from 'react';


import Home from "./components/Home"
class App extends Component {

  state = {
    city : '',
    stores : []
  }

  render() {
    return (
      <Home />
      );
  }
}

export default App;
