import React, { Component } from 'react';
import Buscador from "./components/Buscador";
import Resultado from "./components/Resultado";

class App extends Component {

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
      <div className="app container">
        <div className="jumbotron">
          <p className="lead text-center">
            Buscador de tiendas
          </p>
          <Buscador
            dataSearch={this.dataSearch}
          />
        </div>
        <Resultado
        stores={this.state.stores}
        />
      </div>
    );
  }
}

export default App;
