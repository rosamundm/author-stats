import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { Button, Form } from "react-bootstrap";
import { createBook } from "./BookTypes";

class CreateBook extends Component {
    constructor(props) {
        super(props);
        this.state = {
            content: ""
        };
    }
    onChange = e => {
        this.setState({ [e.target.name]: e.target.value });
    };

    onCreateClick = () => {
        const book = {
            content: this.state.content
        };
        this.props.createBook(book);
    };

    render() {
        return (
            <div>
                <h2>Create new book</h2>
                <Form>
                    <Form.Group controlId="contentID">
                        <Form.Label>Note</Form.Label>
                        <Form.Control
                          as="textarea"
                          rows={3}
                          name="content"
                          placeholder="XYZ"
                          value={this.content}
                          onChange={this.onChange}
                        />
                    </Form.Group>
                </Form>
                <Button variant="success" onClick={this.onAddClick}>Send</Button>
            </div>
        );
    }
}

createBook.PropTypes = {
    createBook: PropTypes.func.isRequired
};

const mapStateToProps = state => ({});

export default connect(mapStateToProps, { createBook })(withRouter(AddBook));