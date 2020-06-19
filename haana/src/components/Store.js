import React from 'react';
import Modal from 'react-bootstrap/Modal';
import Button from 'react-bootstrap/Button';
import Parser from 'html-react-parser';
import Product from './Product';
import './../styles/store.css';
import './../styles/card.css';



const Store = (props) => {
    const {name, tags, phone, web_info, description, products} = props.store;    
    const [modalShow, setModalShow] = React.useState(false);
    const score_store = Math.random() * (6 - 3) + 3;
    const stars_fill = '<i class="fa fa-star"></i>';
    const stars_empty = '<i class="fa fa-star grey"></i>';
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
              <div className="col-12 row h-100">
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
              <Button onClick={props.onHide}>Cerrar</Button>
            </Modal.Footer>
          </Modal>
        );
      }

    
    return (
      <div className="container col-sm-6 col-md-6 col-12 col-lg-4">
        <div className="card h-100">
            <div className="card-head">
                <div className="product-detail">
                    <h4>{name.toUpperCase()}</h4>
                </div>
            </div>

            <div className="card-body">
            <div>
              <img src={web_info.logo} alt=""
                     className="product-img"/>
            </div>
              <div className="product-desc">
              <span className="product-caption">
                Calificaci&oacute;n
                <span className="product-rating">
                {Parser(stars_fill.repeat(score_store))}
                {Parser(stars_empty.repeat(6 - score_store))}
              </span>
              </span>
                  <span className="product-title">
                  <b>Especialistas en:</b>
                  {tags.map(function(tag, i){
                    return <span className="badge" key={i}>{tag}</span>
                      })
                    }
              </span>
            </div>
            <div className="product-properties">
              <span className="product-size">
                    <h4>{description}<br></br><br></br></h4>
              </span>
              <div className="phone">
                  <span>Telefono: {phone} </span>
                  <a className="product-price" href={"https://api.whatsapp.com/send?phone=+57" + phone} target="_blank">
                        <img border="0" alt=""
                        src="https://icons.iconarchive.com/icons/dtafalonso/android-l/256/WhatsApp-icon.png" 
                        width="30px" height="30px"></img>
                  </a>
              </div>
            </div>
            <div className="button_store block" >
                  <Button block variant="primary" onClick={() => setModalShow(true)}>
                      Ver productos de {name}
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