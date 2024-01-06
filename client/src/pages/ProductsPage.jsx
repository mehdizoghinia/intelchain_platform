import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import { BiPhoneCall } from "react-icons/bi";
import { BsChatLeftText } from "react-icons/bs";

import "./BusinessesPage.css";

const ProductPage = () => {
  const service1Features = [
    "Booking appointments",
    "Explaining images with text using OCR and GPT",
    "Newsletter to customers",
  ];

  const service2Features = [
    "Order placement assistance",
    "Explaining images with text using OCR and GPT",
    "Bot trained on distribution data",
  ];

  return (
    <div className="service-page">
      {" "}
      {/* Enclosing div to control the overall page */}
      <Container>
        <Row className="mt-4">
          {" "}
          {/* Added margin-top using Bootstrap class mt-4 */}
          <Col className="service-section">
            <h1>Service 1</h1>
            <BiPhoneCall size={100} />
            <p>Name of Service: Customer Service (Voice Call)</p>
            <h4>Features:</h4>
            <ul>
              {service1Features.map((feature, index) => (
                <li key={index}>{feature}</li>
              ))}
            </ul>
          </Col>
          <Col className="service-section">
            <h1>Service 2</h1>
            <BsChatLeftText size={100} />

            <p>Name of Service: Customer Service (WhatsApp Chat)</p>
            <h4>Features:</h4>
            <ul>
              {service2Features.map((feature, index) => (
                <li key={index}>{feature}</li>
              ))}
            </ul>
          </Col>
        </Row>
      </Container>
    </div>
  );
};

export default ProductPage;
