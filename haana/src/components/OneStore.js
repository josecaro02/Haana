import React, { Component } from 'react';

class OneStore extends Component {
    state = {
        data : [],
        stores : [],
        id : ''
      }
      componentDidMount() {
        const id = document.location.pathname.split('/')
        const url = `http://54.157.184.202/api/stores/${id[2]}`;
        fetch(url)
          .then(response => response.json())
          .then(data => this.setState({ data }));
      }
      render() {
        var products = this.state.data.products ;
        console.log(products);
        return (
          <div>
          <h1>{this.state.data.name}</h1>
        <h1>{this.state.data.type}</h1>
        <h1>{this.state.data.sub_type}</h1>
        </div>
        );
      }
}
 
export default OneStore;