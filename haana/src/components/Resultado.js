import React, { Component } from 'react';
import Store from './Store';
import './../styles/resultado.css';

class Resultado extends Component {

    scroll = () => {
        const element = document.querySelector('.results');
        element.scrollIntoView({behavior: "smooth", block: "start"});
    }
    show_stores = () => {
        const stores = this.props.stores;
        if (stores.length === 0) return null;

        console.log(stores);
        return (
            <React.Fragment>
                <div className="col-12 p-5 row resultado">
                    {stores.map(store => (
                          <Store
                            key={store._id}
                            store={store}
                            josevar="hola"
                          />     
                    ))}
                </div>
            </React.Fragment>
        )
    }
    componentWillUpdate() {
        this.scroll();
    }
  
    render() { 
        return (
            <React.Fragment>
                <div className="results">
                {this.show_stores()}
                </div>
            </React.Fragment>
          );
    }
}
 
export default Resultado;