import React, { Component } from 'react';
import logo from "./../media/logo.png";
import './../styles/home.css';

class Buscador extends Component {

    searchRef = React.createRef();


    getStores = (e) => {
        e.preventDefault();

        const valueSearch = this.searchRef.current.value;

        this.props.dataSearch(valueSearch);
    }

    render() { 
        return (  
            <form onSubmit={this.getStores}>
                <div className="row" id="results">
                    <div className="form-group col-md-2  col-sm-12">
                        <img className="center" src={logo} alt=''></img>
                    </div>    
                    <div className="form-group col-md-8 mt-0 mt-md-4">
                        <input ref={this.searchRef} type="text" className="form-control form-control-lg"
                            placeholder="Ingresa el nombre de tu ciudad"/>
                    </div>
                    <div className="form-group col-md-2 mt-0 mt-md-4">
                        <input type="submit" className="btn btn-lg btn-warning btn-block"
                            value="Buscar"/>
                    </div>
                </div>
            </form>
        );
    }
}
 

export default Buscador;