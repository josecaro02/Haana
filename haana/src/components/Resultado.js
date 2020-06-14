import React, { Component } from 'react';
import Store from './Store'

class Resultado extends Component {
    show_stores = () => {
        const stores = this.props.stores;
        if (stores.length === 0) return null;

        console.log(stores);
        return (
            <React.Fragment>
                <div className="col-12 p-5 row">
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
    render() { 
        return (
            <React.Fragment>
                {this.show_stores()}
            </React.Fragment>
          );
    }
}
 
export default Resultado;