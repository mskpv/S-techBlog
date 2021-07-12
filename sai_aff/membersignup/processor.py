from django.conf import settings

from .models import Visitor_Infos
import datetime

import socket
import random

def save_visitor_infos(request):
    try:
        #----- get visitor ip -----#
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')    
        #----- check if ip adress is valid -----#
        try:
            socket.inet_aton(ip)
            ip_valid = True
        except socket.error:
            ip_valid = False
        #----- check if ip adress is valid -----#
        if ip_valid:

            present_date = datetime.datetime.now()
            ref_date_1 = present_date - datetime.timedelta(days=1)
            ref_date_2 = present_date - datetime.timedelta(days=2)

            if Visitor_Infos.objects.filter(ip_address=ip, page_visited=request.path, event_date__gte=ref_date_1).count() == 0:
                new_visitor_infos = Visitor_Infos(
                ip_address = ip,
                page_visited = request.path,
                event_date = present_date)          
                new_visitor_infos.save()

            if Visitor_Infos.objects.filter(ip_address=ip, page_visited=request.path, event_date__gte=ref_date_1).count() == 1:
                visitor_infos_obj = Visitor_Infos.objects.get(ip_address=ip, page_visited=request.path, event_date__gte=ref_date_1)
                visitor_infos_obj.event_date = present_date
                visitor_infos_obj.save()
    except:
        pass

    d1_nb_vistors = 0
    d1_date = present_date - datetime.timedelta(minutes=5)
    d7_date = present_date - datetime.timedelta(days=7)
    d30_date = present_date - datetime.timedelta(days=30)
    d90_date = present_date - datetime.timedelta(days=90)
    d180_date = present_date - datetime.timedelta(days=180)


    d1_nb_vistors = Visitor_Infos.objects.filter(event_date__gte=d1_date).values_list('ip_address', flat=True).distinct().count()
    d7_nb_vistors = Visitor_Infos.objects.filter(event_date__gte=d7_date).values_list('ip_address', flat=True).distinct().count()
    d30_nb_vistors = Visitor_Infos.objects.filter(event_date__gte=d30_date).values_list('ip_address', flat=True).distinct().count()
    d90_nb_vistors = Visitor_Infos.objects.filter(event_date__gte=d90_date).values_list('ip_address', flat=True).distinct().count()
    d180_nb_vistors = Visitor_Infos.objects.filter(event_date__gte=d180_date).values_list('ip_address', flat=True).distinct().count()
    total_nb_vistors = Visitor_Infos.objects.values_list('ip_address', flat=True).distinct().count()

    context = {
        'd1_nb_vistors': d1_nb_vistors, 
        'd7_nb_vistors': d7_nb_vistors, 
        'd30_nb_vistors': d30_nb_vistors, 
        'd90_nb_vistors': d90_nb_vistors, 
        'd180_nb_vistors': d180_nb_vistors, 
        'total_nb_vistors': total_nb_vistors,
    }

    return context