import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";

import { Container, Navbar, Nav } from "react-bootstrap";

import BookList from ".../mybooks/BookList";
import CreateBook from ".../mybooks/CreateBook";

class Dashboard extends Component {
    render () {
        const { user } = this.props.auth;
        return (
            <div>
                <Navbar bg="light">
                    <Navbar.Brand href="/">Home</Navbar.Brand>
                    <Navbar.Toggle />
                    <Navbar.Collapse className="justify-content-end">
                        <Navbar.Text>
                            I guess this worked?
                        </Navbar.Text>
                    </Navbar.Collapse>
                </Navbar>
                <Container>
                    {/* something */}
                    <BookList />
                    <AddBook />
                </Container>
            </div>
        );
    }
}

/*
Dashboard.propTypes = {
    logout: PropTypes.func.isRequired,
    auth: PropTypes.object.isRequired
};

const mapStateToProps = state => ({
    auth: state.auth
});
*/

export { Dashboard };

