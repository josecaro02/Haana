import React from 'react';
import './../styles/product.css';

const Product = (props) => {

    const {name, description, img_link, value} = props.product;

    return (
        <div className="col-12 col-sm-12 col-md-6 col-lg-6 col-xl-4 mb-4">
        <div className="card border-warning">
            <h4 className="card-header">{name}</h4>
            <div className="store_img">
                  <img src={img_link} alt=""/>
            </div>
            <div className="card-body">
                <p>Description:<br></br>{description}</p>
                <h4>Value: {value}</h4>
            </div>
        </div>
        </div>
    );
}
export default Product;