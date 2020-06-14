import React, { Component } from 'react';

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
                <div className="row">
                    <div className="form-group col-md-8">
                        <input ref={this.searchRef} type="text" className="form-control form-control-lg"
                            placeholder="Search restaurants in your city"/>
                    </div>
                    <div className="form-group col-md-4">
                        <input type="submit" className="btn btn-lg btn-danger btn-block"
                            value="Search"/>
                    </div>
                </div>
            </form>
        );
    }
}
 

export default Buscador;