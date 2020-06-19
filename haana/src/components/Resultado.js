import React, { Component } from 'react';
import Store from './Store';

class Resultado extends Component {

    scroll = () => {
        const element = document.querySelector('.results');
        element.scrollIntoView({behavior: "smooth", block: "start"});
    }
    show_stores = () => {
        const stores = this.props.stores;
        if (stores.length === 0) return null;

         return (
            <React.Fragment>
                <div className="col-12 p-5 row resultado">
                    {stores.map(store => (
                          <Store
                            key={store._id}
                            store={store}
                          />     
                    ))}
                </div>
            </React.Fragment>
        )
    }
    componentDidUpdate() {
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