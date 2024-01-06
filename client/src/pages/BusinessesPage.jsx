import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import "./BusinessesPage.css";

const BusinessesPage = () => {

  return (
    <>
      <Container>
        <Row>
          <Col className="mg-top text-center">
            <h1>Our partners</h1>
            <hr className="hr-text" />
          </Col>
        </Row>
      </Container>
    </>
  );
};

export default BusinessesPage;
