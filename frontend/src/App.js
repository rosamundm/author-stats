import React, { Component } from 'react';
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      bookList: [],
      activeItem: {
        id: "",
        title: "",
        date_added: "",
        wordcount: "",
        goalwordcount: "",
      }
    };
  }

  componentDidMount() {
    this.refreshBookList();
  }

  refreshBookList = () => {
    axios
      .get("/api/v1/books/")
      .then((res) => this.setState({ bookList: res.data}))
      .catch((err) => console.log(err));
  };

  handleSubmit = (item) => {
    this.toggle();

    if (item.id) {
      axios
        .put(`/api/v1/books/${item.id}`)
        .then((res) => this.refreshBookList());
      return;
    }

    axios
      .post("/api/v1/books/", item)
      .then((res) => this.refreshBookList());
  };

  handleDelete = (item) => {
    axios
      .delete(`/api/v1/books/${item.id}`)
      .then((res) => this.refreshBookList());
  };

  createItem = () => {
    const item = { title: "", wordcount: "", goalwordcount: "" };
    // this.setState({ activeItem: item });
  };

  renderItems = () => {
    const newItems = this.state.bookList.filter(
      (item) => item.wordcount > 0
    );

    return newItems.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className="book-title"
          title={item.title}
        >
        </span>

        <span>
          <button
            className="btn btn-secondary mr-2"
            onClick={() => this.handleDelete(item)}
          >
            Delete
          </button>
        </span>
      </li>
    ));
  };


  render () {
    return (
      <main className="container">
        <h1 className="text-black text-uppercase text-center my-4">my book list</h1>
        <div className="row">
          <button
            className="btn btn-primary"
            onClick="{this.createItem}"
          >
            Add book
          </button>
        </div>
        <ul className="list-group list-group-flush border-top-0">
          {this.renderItems()}
        </ul>
      </main>
    );
  }
}

export default App;
