from hashlib import new
from multiprocessing import context
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from .models import *
from website.models import *
from .models import Achivements as DepAchievements

# Create your views here.


def getDepartment(department):
    match department:
        case "BSH":
            return "Basic Science and Humanities"
        case "CSE":
            return "Computer Science and Engineering"
        case "ECE":
            return "Electronics and Communication Engineering"
        case "EEE":
            return "Electrical and Electronics Engineering"
        case "ME":
            return "Mechanical Engineering"
        case "CE":
            return "Civil Engineering"


class Context:
    """This class is used to pass context to the templates"""

    def __init__(self, dep, route):
        self.dep = dep
        self.title = getDepartment(dep)
        self.updates = HomeUpdates.objects.all()
        self.hero_image = DepHero.objects.all().filter(department=dep).first()
        self.dep_updates = DepUpdates.objects.filter(department=dep)
        self.contact = Contact.objects.filter(department=dep)
        self.route = route
        self.about = DepAbout.objects.filter(department=dep).filter(page=route).first()
        self.faculties = None
        self.HOD = None
        self.vission = None
        self.mission = None
        self.objectives = None
        self.poes = None
        self.pos = None
        self.psos = None
        self.associations = None
        self.professional_bodies = None
        self.syllabus = None
        self.labs = None
        self.events = None
        self.achivements = None
        self.newsletters = None
        self.dab = None
        self.dab_data = None
        self.pac = None
        self.pac_data = None
        self.gallery = Gallery.objects.filter(department=dep)[:10]
        match route:
            case "about":
                self.vission = Vission.objects.filter(department=dep).first()
                self.objectives = Objectives.objects.filter(department=dep)
                self.mission = Mission.objects.filter(department=dep)
                self.poes = POES.objects.filter(department=dep)
                self.pos = POS.objects.filter(department=dep)
                self.psos = PSOS.objects.filter(department=dep)
                self.faculties = (
                    Faculty.objects.filter(department=dep)
                    .exclude(role__role="HOD")
                    .order_by("priorities")
                )
                self.HOD = (
                    Faculty.objects.filter(department=dep)
                    .filter(role__role="HOD")
                    .first()
                )
            case "faculty":
                self.faculties = (
                    Faculty.objects.filter(department=dep)
                    .exclude(role__role="HOD")
                    .order_by("priorities")
                )
                self.HOD = (
                    Faculty.objects.filter(department=dep)
                    .filter(role__role="HOD")
                    .first()
                )
            case "associations":
                self.associations = Associations.objects.filter(department=dep)
            case "curriculum_and_syllabus":
                self.syllabus = SyllabusPDFS.objects.filter(department=dep)
            case "professionalBodies":
                self.professional_bodies = ProfessionalBodies.objects.filter(
                    department=dep
                )
            case "labs":
                self.labs = Laboratories.objects.filter(department=dep)
            case "events":
                self.events = Events.objects.filter(department=dep).order_by("-date")
            case "achievements":
                self.achivements = DepAchievements.objects.filter(department=dep)
            case "newsletters":
                self.newsletters = NewsLetters.objects.filter(department=dep)
            case "DAB":
                self.dab = DAB.objects.filter(department=dep).first()
                print(self.dab)
                self.dab_data = DabTable.objects.filter(department=dep)
            case "PAC":
                self.pac = PAC.objects.filter(department=dep).first()
                self.pac_data = PacTable.objects.filter(department=dep)


    def data(self):
        """This method returns the context"""
        return {
            "dep": self.dep,
            "title": self.title,
            "about": self.about,
            "gallery": self.gallery,
            "updates": self.updates,
            "route": self.route,
            "faculties": self.faculties,
            "HOD": self.HOD,
            "hero_img": self.hero_image,
            "dep_updates": self.dep_updates,
            "vission": self.vission,
            "objectives": self.objectives,
            "mission": self.mission,
            "poes": self.poes,
            "pos": self.pos,
            "psos": self.psos,
            "associations": self.associations,
            "professional_bodies": self.professional_bodies,
            "syllabus": self.syllabus,
            "labs": self.labs,
            "events": self.events,
            "achivements": self.achivements,
            "contact": self.contact,
            "newsletters": self.newsletters,
            "dab": self.dab,
            "dab_data": self.dab_data,
            "pac": self.pac,
            "pac_data": self.pac_data,
        }


def home(request):
    return redirect("CSE/about")


def Department(request, route, department):
    context = Context(department, route).data()
    match route:
        case "about":
            return render(request, "Departments/index.html", context)
        case "faculty":
            return render(request, "Departments/Faculty.html", context)
        case "associations":
            return render(request, "Departments/Associations.html", context)
        case "professionalBodies":
            return render(request, "Departments/ProfessionalBodies.html", context)
        case "labs":
            return render(request, "Departments/Laboratories.html", context)
        case "achievements":
            if request.method == "GET":
                year = request.GET.get("year")
                default_year = ACADEMIC_YEARS[0][0]
                default_type = "faculty"
                a_type = request.GET.get("type")
                context["allYears"] = [
                    nested_tuple[0] for nested_tuple in ACADEMIC_YEARS
                ]
                context["defaultYear"] = default_year
                context["type"] = a_type
                if year and a_type:
                    context["achivements"] = (
                        DepAchievements.objects.filter(department=department)
                        .filter(year=year)
                        .filter(type=a_type)
                    )
                    return render(
                        request, "Departments/Achievements.html", context=context
                    )
                else:
                    context["achivements"] = (
                        DepAchievements.objects.filter(department=department)
                        .filter(year=default_year)
                        .filter(type=default_type)
                    )
                    return render(
                        request, "Departments/Achievements.html", context=context
                    )
            else:
                return Http404("Page Not Found")

        case "events":
            if request.method == "GET":
                year = request.GET.get("year")
                context["allYears"] = [
                    nested_tuple[0] for nested_tuple in ACADEMIC_YEARS[::-1]
                ]
                if year :
                    if year == "ALL":
                        context["all_events"] = Events.objects.filter(department=department).all()
                    else:
                        context["all_events"] = Events.objects.filter(department=department).filter(year=year)
                    return render(request, "Departments/Events.html", context=context)
                else:
                    context["all_events"] = (
                        Events.objects.filter(department=department).all()
                    )
                    return render(
                        request, "Departments/Events.html", context=context
                    )
            else:
                return Http404("Page Not Found")
        case "curriculum_and_syllabus":
            return render(request, "Departments/curriculum_and_syllabus.html", context)
        case "newsletters":
            return render(request, "Departments/NewsLetters.html", context)
        case "innovative_tlm":
            context["innovative_tlm"] = InnovativeTLM.objects.filter(
                department=department
            ).all()
            context["tlm_table"] = TLM_table.objects.filter(
                tlm_method__department=department
            ).all()
            return render(request, "Departments/innovative_tlm.html", context)
        case "research":
            return redirect("dep_research", department, "index")

        case "DAB":
            return render(request, "Departments/DAB.html", context)

        case "PAC":
            return render(request, "Departments/PAC.html", context)
        
        case "students":
            context["students"] = Students.objects.filter(department=department).order_by("-year") 
            return render(request, "Departments/Students.html", context)


        case "StreamCommittee":
            if request.method == "GET":
                stream = request.GET.get("stream")
                default_stream = Streams.objects.filter(department=department).first().id
                context["streams"] = Streams.objects.filter(department=department)
                context["defaultStream"] = default_stream
                if stream:
                    context["sel_stream"] = Streams.objects.filter(id=stream).first()
                    context["stream_com"] = StreamComm.objects.filter(
                        stream__department=department
                    ).filter(stream=stream)
                    return render(
                        request, "Departments/StreamCommittee.html", context=context
                    )
                else:
                    context["sel_stream"] = Streams.objects.filter(id=default_stream).first()
                    context["stream_com"] = StreamComm.objects.filter(
                        stream__department=department
                    ).filter(stream=default_stream)
                    return render(
                        request, "Departments/StreamCommittee.html", context=context
                    )
            else:
                return Http404("Page Not Found")

        case other:
            raise Http404("Page Not Found")


def research_page(request, department, slug):
    hero_image = DepHero.objects.all().filter(department=department).first()
    context_temp = {
        "dep": department,
        "route": "research",
        "slug": slug,
        "hero_img": hero_image,
    }
    match slug:
        case "index":
            hero_title = "Research"
            context = {"hero_title": hero_title, **context_temp}
            return render(request, "Departments/research/index.html", context)
        case "consultancy":
            context = {
                "hero_title": "Academic Consultancy",
                "academic_consultancy": AcademicConsultancy.objects.all().filter(
                    department=department
                ),
                **context_temp,
            }
            return render(
                request, "Departments/research/academic_consultancy.html", context
            )
        case "parternship":
            context = {
                "hero_title": "Academic Partnership",
                "academic_partnership": AcademicPartnerShip.objects.all().filter(
                    department=department
                ),
                **context_temp,
            }
            return render(
                request, "Departments/research/academic_partnership.html", context
            )
        case "conference":
            context = {
                **context_temp,
                "hero_title": "Conference & Symposium ",
                "conferences": Conference.objects.all().filter(department=department),
            }
            return render(request, "Departments/research/conference.html", context)
        case "funded_projects":
            context = {
                **context_temp,
                "hero_title": "Funded Projects",
                "funded_projects": FundedProjects.objects.all().filter(
                    department=department
                ),
            }
            hero_title = "Funded Projects"
            return render(request, "Departments/research/funded_projects.html", context)
        case "publications":
            publications = FacultyStudentPublications.objects.all().filter(
                dep=department
            )
            context = {
                **context_temp,
                "hero_title": "Publications",
                "publications": publications,
            }
            return render(request, "Departments/research/publications.html", context)
        case "research_guides":
            research_guides = ResearchGuides.objects.all().filter(
                faculty__department=department
            )
            context = {
                **context_temp,
                "hero_title": "KTU Approved RESEARCH GUIDES",
                "research_guides": research_guides,
            }

            return render(request, "Departments/research/research_guides.html", context)
        case other:
            raise Http404("Page Kanumanilla")


def ProfessionalBodie(request, slug):
    context = {
        "professional_body": ProfessionalBodies.objects.filter(id=slug).first(),
        "events": ProfessionalBodiesEvents.objects.filter(ProfessionalBodies_id=slug),
        "members": ProfessionalBodiesTeamMembers.objects.filter(
            ProfessionalBodies_id=slug
        ).order_by("priority"),
        "gallery": Gallery.objects.all().order_by("?")[:6],
    }
    return render(
        request, "Departments/professsionalbody_showcase.html", context=context
    )


def Association(request, slug):
    context = {
        "association": Associations.objects.filter(id=slug).first(),
        "events": AssociationsEvents.objects.filter(assosiation_id=slug),
        "members": AssociationTeamMembers.objects.filter(assosiation_id=slug).order_by(
            "priority"
        ),
        "gallery": Gallery.objects.all().order_by("?")[:6],
    }
    return render(request, "Departments/association_showcase.html", context)
