import React from "react";
import { Button, Container } from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";
// import Title from "../components/Title";

const HomePage = () => {
  return (
    <>
      {/* <Title /> */}
      <header className="masthead main-bg-image">
        <Container className="px-4 px-lg-5 d-flex h-100 align-items-center justify-content-center">
          <div className="d-flex justify-content-center">
            <div className="text-center">
              <h1 className="display-4 text-center text-white font-weight-bold">
                intelChain
              </h1>

              <h2 className="text-white-50 mx-auto mt-2 mb-5">
                Bring AI customer service to your business and Automate 75%
                percent of your job with our bots and just focus on the rest.
              </h2>
              <LinkContainer to="/businesses">
                <Button variant="primary">Get Started</Button>
              </LinkContainer>
            </div>
          </div>
        </Container>
      </header>
    </>
  );
};

export default HomePage;
