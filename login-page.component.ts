import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.scss']
})
export class LoginPageComponent implements OnInit {

  user: string = "";
  password: string ="";

  constructor(private http: HttpClient) { 
    
  }

  ngOnInit(): void {
  }

  confirmation() {
    let bodyData = {
      "user": this.user,
      "password": this.password
    };

  this.http.post("http://127.0.0.1:5000/login", bodyData).subscribe((resultData: any)=> {
    console.log(resultData);
    alert("success");
  });
  }


}
