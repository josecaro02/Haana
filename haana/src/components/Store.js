import React from 'react';
import Modal from 'react-bootstrap/Modal';
import Button from 'react-bootstrap/Button';
import Product from './Product';
import './../styles/store.css';


const Store = (props) => {
    const {name, sub_type, phone, web_info, description, products} = props.store;
    
    const [modalShow, setModalShow] = React.useState(false);
    console.log(products);
    function MyVerticallyCenteredModal(props) {
 
         return (

          <Modal
            {...props}
            size="lg"
            aria-labelledby="contained-modal-title-vcenter"
            centered
          >
            <Modal.Header closeButton>
              <Modal.Title id="contained-modal-title-vcenter">
                {name}
              </Modal.Title>
            </Modal.Header>
            <Modal.Body>
              <p>
                {description}
              </p>
              <React.Fragment>
              <div className="col-12 row">
                {products.map(product => (
                  <Product
                    key={product.name} 
                    product={product}
                  /> 
                ))}  
              </div>
              </React.Fragment>
            </Modal.Body>
            <Modal.Footer>
              <Button onClick={props.onHide}>Close</Button>
            </Modal.Footer>
          </Modal>
        );
      }

    
    return (

        <div className="col-12 col-sm-12 col-md-6 col-lg-6 col-xl-4 mb-4">
            <div className="card border-warning">
                <h4 className="card-header">{name}</h4>
                <div className="store_img">
                  <img src={web_info.logo} alt="" className="card-img-top"/>
                </div>
                <div className="card-body">
                    <h5 className="card-text">Specialized in:<br></br> 
                        <span className="badge badge-danger">{sub_type}</span>
                    </h5>
                <h5 className="card-text">Phone: {phone}</h5>
                <div className="button_store" >
                  <Button block variant="primary" onClick={() => setModalShow(true)}>
                      Show {name}
                  </Button>
                </div>
                <MyVerticallyCenteredModal
                    show={modalShow}
                    onHide={() => setModalShow(false)}
                />
                </div>
            </div>
        </div>


    )
}

export default Store;