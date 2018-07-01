import React, { Component } from "react";
import CommentsBox from "./presenter";

class Container extends Component {
  state = {
    comment: ""
  };
  render() {
    return (
      <CommentsBox 
        { ...this.state } 
        handleInputChange={this._handleInputChange} 
        handleKeyPress={this._handleKeyPress}
      />
    );
  }
  _handleInputChange = event => {
    const { target:  { value } } = event;
    this.setState({
      comment: value
    });
  };
  _handleKeyPress = event => {
    const { key } = event;
    if(key === "Enter") {
      event.preventDefault(); // 텍스트 입력창에 엔터로 새로운 줄 생성 되는것 막는 것
    }
    console.log(key);
  };
}

export default Container;
