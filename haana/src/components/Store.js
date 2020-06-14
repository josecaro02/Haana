import React from 'react';

const Store = (props) => {

    const {name, sub_type, phone, web_info} = props.store;
    return (
        <div className="col-12 col-sm-6 col-md-4 col-lg-3 mb-4">
            <div className="card border-info">
                <h3 className="card-header">{name}</h3>
                <img src={web_info.logo} alt="" className="card-img-top"/>
                <div className="card-body">
                    <h5 className="card-text">Specialized in:<br></br> 
                        <span class="badge badge-danger">{sub_type}</span>
                    </h5>
                    <p className="card-text">Description:<br></br>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean vel eros eu elit fermentum commodo ut in risus.
                    </p>
                <h5 className="card-text">Phone: {phone}</h5>
                <a href="#" class="btn btn-info btn-block">Go to {name}</a>
                </div>
            </div>
        </div>
    )
}

export default Store;