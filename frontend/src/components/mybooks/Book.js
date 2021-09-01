import React, { Component } from "react";
import PropTypes from "prop-types";

class Book extends Component {
    render() {
        const { book } = this.props;
        return (
            <div>
                <p>{book.content}</p>
            </div>
        );
    }
}

Book.PropTypes = {
    book: PropTypes.object.isRequired
};
export default Book;