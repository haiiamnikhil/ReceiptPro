import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs'

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  httpHeaders = new HttpHeaders({'Content-Type': 'application/json'})

  constructor(private http: HttpClient) { }

  loginUser(user:any):Observable<any> {
    return this.http.post('/loginform/', user,{headers: this.httpHeaders})
  }

  getUserDetails():Observable<any>{
    return this.http.get('/details/',{headers: this.httpHeaders})
  }

  logoutUser():Observable<any>{
    return this.http.post('/logout/',{headers: this.httpHeaders})
  }

  isUser():Observable<any>{
    return this.http.post('/details/',{headers: this.httpHeaders})
  }

  getPresentUser():Observable<any>{
    return this.http.get('/details/',{headers: this.httpHeaders})
  }

  getAllUsers():Observable<any>{
    return this.http.get('/listuserview/',{headers: this.httpHeaders})
  }

  isSamePresentUser():Observable<any>{
    return this.http.get('/isSameUser/',{headers: this.httpHeaders})
  }

  getEmpDetails(username:any):Observable<any>{
    return this.http.post('/emp-profile/view/'+username+'/',{headers: this.httpHeaders})
  }

  uploadData(data:any):Observable<any>{
    return this.http.post('/fileupload/upload/doc/',data)
  }
}