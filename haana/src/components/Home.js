import React, { Component } from 'react';
import Buscador from "./Buscador";
import Resultado from "./Resultado";
import './../styles/home.css';

class Home extends Component {
    state = {
    city : '',
    stores : []
  }

  getApi = () => {
    const url = `http://54.157.184.202/api/location/${this.state.city}`;
    
    fetch(url).then(respuesta => respuesta.json() ).then(resultado => this.setState({stores : resultado}))
  }

  dataSearch = (city) => {
    this.setState({
      city
    }, () => {
      this.getApi();
    })
  }
  render() {
    return (
      <div className="app container-fluid" id="principal">
        <div>
          <div className="main-info">
            <h1>Welcome to Haana</h1>
            <h4>Hanna helps you to find all the stores's information in your city</h4>
          </div>
          <div className="jumbotron">
            <Buscador
              dataSearch={this.dataSearch}
            />
          </div>
        </div>  
        <div className="resultado-block">
        <Resultado
          stores={this.state.stores}
        />
      </div>  
      </div>

    );
  }

}

export default Home;
