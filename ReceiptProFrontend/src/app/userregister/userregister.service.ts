import { HttpClient,HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserregisterService {
  // private baseUrl = 'http://127.0.0.1:8000';
  httpHeaders = new HttpHeaders({'Content-Type': 'multipart/form-data'})

  constructor(private http: HttpClient) { }

  listUsers():Observable<any>{
    return this.http.get('/register/',{headers:this.httpHeaders})
  }
  
  register(data): Observable<any>{
    return this.http.post('/registerform/', data)
  }

}
