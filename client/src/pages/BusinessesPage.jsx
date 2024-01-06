import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import "./BusinessesPage.css";

const BusinessesPage = () => {
  // Sample data of businesses
  const businesses = [
    {
      businessName: "Example Clinic",
      owner: "Dr. Smith",
      phoneNumber: "123-456-7890",
      location: "City, State",
      services: [
        {
          serviceName: "Customer Service (Voice Call)",
          features: ["Booking appointments"],
        },
        {
          serviceName: "Customer Service (WhatsApp Chat)",
          features: [
            "Booking appointments",
            "Explaining prescriptions in images using OCR and GPT",
            "Bot trained on clinic data",
          ],
        },
      ],
    },
    {
      businessName: "Sample Farm",
      owner: "John Doe",
      phoneNumber: "987-654-3210",
      location: "City, State",
      services: [
        {
          serviceName: "Customer Service (Voice Call)",
          features: ["Newsletter to customers", "Bot trained on farm data"],
        },
        {
          serviceName: "Customer Service (WhatsApp Chat)",
          features: [
            "Booking farm visits",
            "Explaining items in images using OCR and GPT",
            "Bot trained on farm data",
          ],
        },
      ],
    },
    {
      businessName: "Test Distribution",
      owner: "Jane Smith",
      phoneNumber: "111-222-3333",
      location: "City, State",
      services: [
        {
          serviceName: "Customer Service (Voice Call)",
          features: [
            "Order placement assistance",
            "Bot trained on distribution data",
          ],
        },
        {
          serviceName: "Customer Service (WhatsApp Chat)",
          features: [
            "Order placement assistance",
            "Explaining items in  images using OCR and GPT",
            "Bot trained on distribution data",
          ],
        },
      ],
    },
    {
      businessName: "HealthCare Solutions",
      owner: "Dr. Anderson",
      phoneNumber: "444-555-6666",
      location: "City, State",
      services: [
        {
          serviceName: "Customer Service (Voice Call)",
          features: [
            "Medical appointment scheduling",
            "Bot trained on healthcare data",
          ],
        },
        {
          serviceName: "Customer Service (WhatsApp Chat)",
          features: [
            "Medical appointment scheduling",
            "Healthcare information via images with OCR and GPT",
            "Bot trained on healthcare data",
          ],
        },
      ],
    },
  ];

  return (
    <>
      <Container>
        <Row>
          <Col className="mg-top text-center">
            <h1>Our partners</h1>
            <hr className="hr-text" />
          </Col>
        </Row>
        <Row>
          {businesses.map((business, index) => (
            <Col key={index} xl={4} lg={4} md={6} sm={12} className="my-3">
              <div className="business-card">
                <h3>{business.businessName}</h3>
                <p>Owner: {business.owner}</p>
                <p>Phone: {business.phoneNumber}</p>
                <p>Location: {business.location}</p>

                {business.services && business.services.length > 0 && (
                  <div className="services-list">
                    <h4>Services:</h4>
                    <ul>
                      {business.services.map((service, serviceIndex) => (
                        <li key={serviceIndex}>
                          <strong>{service.serviceName}</strong>
                          <ul>
                            <ul>
                              {service.features.map((feature, featureIndex) => (
                                <li key={featureIndex}>
                                  <a href={`#${feature}`} key={featureIndex}>
                                    {feature}
                                  </a>
                                </li>
                              ))}
                            </ul>
                          </ul>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            </Col>
          ))}
        </Row>
      </Container>
    </>
  );
};

export default BusinessesPage;
