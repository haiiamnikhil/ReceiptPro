import { Component, OnInit } from '@angular/core';
import { faCoffee } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-workassign',
  templateUrl: './workassign.component.html',
  styleUrls: ['./workassign.component.css']
})
export class WorkassignComponent implements OnInit {
  presentvalue:number= 1
  keyword = 'name'
  data = [
    {
      id: 1,
      name: 'Usa'
    },
    {
      id: 2,
      name: 'England'
    }
 ];
  names: ['Nikhil','Pradeep']
  constructor() { }

  ngOnInit(): void {
  }

  onIncrement(){
    this.presentvalue += 1
  }

  onDecrement(){
    this.presentvalue -= 1
  }
}
